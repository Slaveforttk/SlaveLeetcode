#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LEVELS 9

void output(int mem[MAX_LEVELS][256], int sizes[MAX_LEVELS]) {
    // 输出
    printf("-----------------------------------------------------------------------------\n");
    for (int i = 0; i < MAX_LEVELS; i++) {
        switch (i) {
        case 0: printf("4KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 1: printf("8KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 2: printf("16KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 3: printf("32KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 4: printf("64KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 5: printf("128KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 6: printf("256KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 7: printf("512KB内存块有%d个，地址分别为：", sizes[i]); break;
        case 8: printf("1024KB内存块有%d个，地址分别为：", sizes[i]); break;
        default: break;
        }
        
        for (int j = 0; j < sizes[i]; j++) {
            printf("%d-%d ", mem[i][j], mem[i][j] + 4 * (int)pow(2, i) - 1);
        }
        printf("\n");
    }
    printf("-----------------------------------------------------------------------------\n\n");
}

void outputProcess(int memTab[256][4], int memTabSize) {
    for (int i = 0; i < memTabSize; i++) {
        printf("进程%d申请了大小为%dKB的空间，首地址为%d，内存块大小为%dKB\n",
               memTab[i][3], memTab[i][1], memTab[i][0], memTab[i][2]);
    }
}

int assignMem(int mem[MAX_LEVELS][256], int sizes[MAX_LEVELS], int processNum, int block, int memTab[256][4], int *memTabSize) {
    int n = 0;
    if (block <= 4)
        n = 0;
    else if (log2(block) == (int)log2(block))
        n = (int)log2(block) - 2;
    else
        n = (int)log2(block) - 1;

    int i = 0;
    if (sizes[n] == 0) {
        for (i = n + 1; i < MAX_LEVELS; i++) {
            if (sizes[i] != 0)
                break;
        }
        if (i == MAX_LEVELS) {
            printf("没有足够的内存可以分配\n");
            return 0;
        }
        int addressTotal = mem[i][0];
        for (int j = 0; j < sizes[i] - 1; j++)
            mem[i][j] = mem[i][j + 1];
        sizes[i]--;
        
        for (int j = 0; j < i - n; j++)
            mem[i - j - 1][sizes[i - j - 1]++] = addressTotal + 4 * pow(2, i - j) / 2;
        
        memTab[*memTabSize][0] = addressTotal;
        memTab[*memTabSize][1] = block;
        memTab[*memTabSize][2] = 4 * (int)pow(2, n);
        memTab[*memTabSize][3] = processNum;
        (*memTabSize)++;
        return 1;
    } else {
        int addressTotal = mem[n][0];
        for (int j = 0; j < sizes[n] - 1; j++)
            mem[n][j] = mem[n][j + 1];
        sizes[n]--;
        
        memTab[*memTabSize][0] = addressTotal;
        memTab[*memTabSize][1] = block;
        memTab[*memTabSize][2] = 4 * (int)pow(2, n);
        memTab[*memTabSize][3] = processNum;
        (*memTabSize)++;
        return 1;
    }
}

void releaseMemProcess(int mem[MAX_LEVELS][256], int sizes[MAX_LEVELS], int level, int address) {
    if (address / (int)(4 * pow(2, level)) % 2 == 0) {
        int j = level;
        if (sizes[j] == 0) {
            mem[j][sizes[j]++] = address;
        } else {
            int k = 0;
            for (k = 0; k < sizes[j]; k++) {
                if (mem[j][k] == address + 4 * pow(2, level))
                    break;
            }
            if (k == sizes[j]) {
                mem[j][sizes[j]++] = address;
            } else {
                for (int m = k; m < sizes[j] - 1; m++)
                    mem[j][m] = mem[j][m + 1];
                sizes[j]--;
                releaseMemProcess(mem, sizes, level + 1, address);
            }
        }
    } else {
        int j = level;
        if (sizes[j] == 0) {
            mem[j][sizes[j]++] = address;
        } else {
            int k = 0;
            for (k = 0; k < sizes[j]; k++) {
                if (mem[j][k] == address - 4 * pow(2, level))
                    break;
            }
            if (k == sizes[j]) {
                mem[j][sizes[j]++] = address;
            } else {
                for (int m = k; m < sizes[j] - 1; m++)
                    mem[j][m] = mem[j][m + 1];
                sizes[j]--;
                releaseMemProcess(mem, sizes, level + 1, address - 4 * pow(2, level));
            }
        }
    }
}

int releaseMem(int mem[MAX_LEVELS][256], int sizes[MAX_LEVELS], int processNum, int memTab[256][4], int *memTabSize) {
    int i = 0;
    for (i = 0; i < *memTabSize; i++) {
        if (memTab[i][3] == processNum)
            break;
    }
    if (i == *memTabSize) {
        printf("不存在编号为%d的进程\n", processNum);
        return 0;
    }

    int j = (int)log2(memTab[i][2] / 4);
    if (memTab[i][0] / memTab[i][2] % 2 == 0) {
        if (sizes[j] == 0) {
            mem[j][sizes[j]++] = memTab[i][0];
        } else {
            int k = 0;
            for (k = 0; k < sizes[j]; k++) {
                if (mem[j][k] == memTab[i][0] + memTab[i][2])
                    break;
            }
            if (k == sizes[j]) {
                mem[j][sizes[j]++] = memTab[i][0];
            } else {
                for (int m = k; m < sizes[j] - 1; m++)
                    mem[j][m] = mem[j][m + 1];
                sizes[j]--;
                releaseMemProcess(mem, sizes, j + 1, memTab[i][0]);
            }
        }
    } else {
        if (sizes[j] == 0) {
            mem[j][sizes[j]++] = memTab[i][0];
        } else {
            int k = 0;
            for (k = 0; k < sizes[j]; k++) {
                if (mem[j][k] == memTab[i][0] - memTab[i][2])
                    break;
            }
            if (k == sizes[j]) {
                mem[j][sizes[j]++] = memTab[i][0];
            } else {
                int address = mem[j][k];
                for (int m = k; m < sizes[j] - 1; m++)
                    mem[j][m] = mem[j][m + 1];
                sizes[j]--;
                releaseMemProcess(mem, sizes, j + 1, address);
            }
        }
    }

    for (int m = i; m < *memTabSize - 1; m++)
        for (int n = 0; n < 4; n++)
            memTab[m][n] = memTab[m + 1][n];
    (*memTabSize)--;
    return 1;
}

int main() {
    int mem[MAX_LEVELS][256] = {0};
    int sizes[MAX_LEVELS] = {0};
    int memTab[256][4] = {0};
    int memTabSize = 0;

    // 初始化
    mem[8][0] = 0;
    sizes[8] = 1;
    output(mem, sizes);

    int block = 0;
    int processNum = 0;
    int function = 0;

    while (1) {
        printf("**********功能选项**********\n\n");
        printf("1申请内存  2释放内存\n\n");
        printf("****************************\n");
        scanf("%d", &function);

        if (function == 1) {
            printf("输入要申请的内存块的大小：");
            scanf("%d", &block);
            if (block == 0)
                break;
            int success = 0;
            if (block <= 1024) {
                success = assignMem(mem, sizes, processNum, block, memTab, &memTabSize);
                if (success == 1) {
                    processNum++;
                    system("cls");
                    output(mem, sizes);
                    outputProcess(memTab, memTabSize);
                }
            } else {
                printf("没有足够的内存可以分配\n");
            }
        } else {
            printf("输入要释放的进程的编号：");
            int procNum = 0;
            scanf("%d", &procNum);
            releaseMem(mem, sizes, procNum, memTab, &memTabSize);
            system("cls");
            output(mem, sizes);
            outputProcess(memTab, memTabSize);
        }
    }

    return 0;
}

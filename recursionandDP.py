def lcs_recursive(seq1,seq2,idx1=0,idx2=0):
    if idx1==len(seq1) or idx2==len(seq2):
        return 0

    elif seq1[idx1]==seq2[idx2]:
        return 1+lcs_recursive(seq1,seq2,idx1+1,idx2+1)
    else:
        option1=lcs_recursive(seq1,seq2,idx1+1,idx2)
        option2=lcs_recursive(seq1,seq2,idx1,idx2+1)
        return max(option1,option2)

print(lcs_recursive('serendipitous','precipitation'))


def lcs_memo(seq1,seq2):
    memo={}
    def recurse(idx1=0,idx2=0):
        key=(idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key]=0
        elif seq1[idx1]==seq2[idx2]:
            memo[key]=1+recurse(idx1+1,idx2+1)
        else:
            memo[key]=max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)

print(lcs_memo('serendipitous','precipitation'))


def lcs_dp(seq1,seq2):
    n1,n2=len(seq1),len(seq2)
    table=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i]==seq2[j]:
                table[i+1][j+1]=1+table[i][j]
            else:
                table[i+1][j+1]=max(table[i+1][j],table[i][j+1])
    return table[-1][-1]

print(lcs_dp('serendipitous','precipitation'))


def max_profit_recursive(weights,profits,capacity,idx=0):
    if idx==len(weights):
        return 0
    elif weights[idx]>capacity:
        return max_profit_recursive(weights,profits,capacity,idx+1)
    else:
        option1=max_profit_recursive(weights,profits,capacity,idx+1)
        option2=profits[idx]+max_profit_recursive(weights,profits,capacity-weights[idx],idx+1)
        return max(option1,option2)

capacity=15
weights=[4, 5, 1, 3, 2, 5]
profits=[2, 3, 1, 5, 4, 7]
print(max_profit_recursive(weights,profits,capacity))


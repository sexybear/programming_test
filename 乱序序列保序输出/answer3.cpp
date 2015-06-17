struct ListNode
{
    int data;
    int len;
    ListNode* next;
};

void InsertNode(ListNode *&pHead, ListNode *pNode)
{
    ListNode * pTmp = NULL;
    if(pNode == NULL)
    {
        cout << "pNode is NULL!" << endl;
        return;
    }
    if(pHead == NULL)
    {
        pHead = pNode;
    }
    else
    {
        for(pTmp = pHead;pTmp->next != NULL; pTmp = pTmp->next)
        ;
        pTmp->next = pNode;
    }
}


void SortAndPrint(int a[], int n)
{
    ListNode *pHead = NULL;
    ListNode *temp = NULL;
    int i = 0;
    int data = 0;
    int dataLen = 0;
    while(i < n)
    {
        int j = 0;
        int len = 0;
        int moreNum = a[i];
        int lessNum = a[i];

        //查找小于一个数的连续数出现次数
        while(j < i)
        {
            if(a[j] == lessNum-1)
            {
                j = 0;
                lessNum--;
                continue;
            }
            j++;
        }

        //只有小于一个数的所有数均出现时才存数据
        if(lessNum == 1)
        {
            j = 0;
            while(j < i)
            {
                if(a[j] == moreNum+1)
                {
                    len++;
                    moreNum++;
                    j = 0;
                    continue;
                }
                j++;
            }

            ListNode *p = (ListNode*)malloc(sizeof(ListNode));
            memset(p, 0, sizeof(ListNode));
            p->data = a[i];
            p->len = len;
            p->next = NULL;
            InsertNode(pHead, p);
        }
        i++;
    }

    //按顺序打印序列
    for(temp=pHead; temp!=NULL; temp=temp->next)
    {
        dataLen = temp->len;
        data = temp->data;
        while(dataLen)
        {
            printf("%d,",data++);
            dataLen--;
        }
        printf("%d\n",data);
    }

    //释放资源
    ListNode *prev = NULL;
    ListNode *curr = pHead;
    while(curr!=NULL)
    {
        prev=curr;
        curr=curr->next;
        if(prev != NULL)
        {
            free(prev);
            prev = NULL;
        }
    }
}

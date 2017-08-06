"""
Bucket sort
Best case: O(n+k) , where loop N element in list and separate to K number of bucket, and concatenate each bucket in the end
Worst case: O(n^2) , if formula for separation of element in bucket result in all element in 1 bucket, bucket sorting will take another O(N)
                     time to sort the bucket
"""
def bucket_sort(list,round_up_greatest_val):
    result_list = [None]*len(list)
    for item in list:
        bucket_index = item * len(list) / round_up_greatest_val     #this formula allow putting element to different "bucket"
        bucket = []

        if result_list[bucket_index] == None:       #if bucket list is not created, initialize new bucket
            bucket.append(item)
            result_list.insert(bucket_index,bucket)
        else:
            bucket = result_list[bucket_index]      #if bucket is created, check which position should it be insert in bucket
            for j in range(0,len(bucket)):
                if item < bucket[j]:
                    bucket.insert(j,item)
                else:
                    bucket.insert(len(bucket)+1,item)
                    break

    result_list = [item for sublist in result_list if sublist != None for item in sublist]  #concatenate sublist in result list *note that here is concatenate with "python way"
    return result_list
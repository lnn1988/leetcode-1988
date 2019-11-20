package main

func merge(nums1 []int, m int, nums2 []int, n int)  {

    if m == 0 {
        for i:=0; i<n; i++ {
            nums1[i] = nums2[i]
        }
        return
    }
    if n == 0 {
        return
    }

    index_1, index_2, index := m-1, n-1, m+n-1
    for index_1 >= 0 && index_2 >= 0{
        if nums1[index_1] >= nums2[index_2]{
            nums1[index] =nums1[index_1]
            index_1 --
        } else {
            nums1[index] =nums2[index_2]
            index_2 --
        }
        index --
    }
    if index_2 >= 0{
        for i:=0;i<=index_2;i++{
            nums1[i] = nums2[i]
        }
    }
}

func main()  {
    nums1 := []int{1,2,3,0,0,0}
    m := 3
    nums2 := []int{0,2,2}
    n := 3
    merge(nums1, m, nums2, n)
}
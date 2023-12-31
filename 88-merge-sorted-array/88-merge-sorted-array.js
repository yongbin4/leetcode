/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// example 
// nums1 = [1, 3, 5, 8, 9]
// nums2 = [2, 4, 6, 7]



var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    
    while (j >= 0) {
        // if the last value of the nums1 is greater than a last value of the nums2
        if (i >= 0 && nums1[i] > nums2[j]) {
            // put the last value of the nums1 to the m + n - 1;
            nums1[k--] = nums1[i--];
        } else {
            // else last value of the nums2 to the m + n - 1;
            nums1[k--] = nums2[j--];
        }
    }
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let j = 1;
    for (let i = 1; i < nums.length; i++){
        // if the lower index is not equal to higher index
        if (nums[i] != nums[j-1]){
            // then lower index is higher index value
            nums[j] = nums[i]
            // increment lower index
            j++
        }
        // else increment higher index 
    }
    return j
};
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const products = [];
        for (let i = 0; i < nums.length; i++) {
            if (i > 0) {
                products[i] = products[i-1] * nums[i-1];
            } else {
                products[i] = 1;
            }
        }
        let rightProduct = 1;
        for (let i = nums.length - 1; i >= 0; i--) {
            products[i] = products[i] * rightProduct;
            rightProduct *= nums[i];
        }

        return products;
    }
}

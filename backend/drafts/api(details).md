



| api                                                          | 请求参数                                                     | 返回值                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| /admin/checkUpShelfRequest                                   |                                                              | 所有商户的上架请求（userName,shopName,name,discription,picture,price,stock,submitStatus) |
| /admin/checkUpShelfRequest/Passed                            | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /admin/checkUpShelfRequest/sentBack                          | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /admin/checkMCIRequest                                       |                                                              | 所有商户的商品信息修改请求（userName,shopName,name,discription,picture,price,stock,submitStatus) |
| /admin/checkMCIRequest/Passed                                | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /admin/checkMCIRequest/sentBack                              | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /merchant/goodsList                                          | shopName(店铺名称)                                           | shopName下的所有商品(name,discription,picture,price,stock,shelf) |
| /merchant/goodsList/add/commit                               | userName(商户名称),shopName(商店名称),name(商品名),discription,picture,price,stock |                                                              |
| /merchant/goodsList/alter/commit                             | userName(商户名称),shopName(商店名称),name(商品名),discription,picture,price,stock |                                                              |
| /merchant/goodsList/delete                                   | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /merchant/goodsList/upShelfRequestList                       | userName(商户名称)                                           | userName的所有上架申请记录(userName,shopName,name,discription,picture,price,stock,submitStatus) |
| /merchant/goodsList/upShelfRequestList/delete                | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| /merchant/goodsList/MCIRequestList                           | userName(商户名称)                                           | userName的所有商品修改申请记录(userName,shopName,name,discription,picture,price,stock,submitStatus) |
| /merchant/goodsList/MCIRequestList/delete                    | userName(商户名称),shopName(商店名称),name(商品名)           |                                                              |
| **新增api:(通过店铺名称shopName得到商家(该店铺所有者)名称userName)  /getUserNameByShopName** | shopName                                                     | userName                                                     |


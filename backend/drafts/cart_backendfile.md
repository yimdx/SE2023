购物车模块的api一览：

| api                         | 后端需要前端传入：                                           | 后端会返回：                                                 | 功能：                                 |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
| `/user/cart`                | `buyerName`                                                  | result（一个字典套了list，list的每一个元素是一个字典）       | 返回该用户购物车中所有商品的数据       |
| `/addingToCart`             | `buyerName`、`merchantName`、`goodsName`、`picture`、`unitprice`、`quantity` | ‘Success’                                                    | 供用户在商店的商品界面添加商品至购物车 |
| `/user/cart/delete`         | `buyerName`、`merchantName`、`goodsName`                     | ‘Success’                                                    | 在用户购物车界面删除商品               |
| `/user/cart/changeQuantity` | `buyerName`、`merchantName`、`goodsName`、`quantity`（所要增减的数量，增加为正数，减少为负数）` | 增减成功返回‘Success’；如果增减后商品数量小于1则返回‘Deleted’ | 在用户购物车界面增减商品               |


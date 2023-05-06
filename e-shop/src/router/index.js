import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminLogin from "../views/Admin/login.vue"
import AdminHome from "../views/Admin/index.vue"
import SellerLogin from "../views/Seller/login.vue"
import SellerHome from "../views/Seller/index.vue"
import BuyerHome from "../views/Buyer/index.vue"
import BuyerLogin from "../views/Buyer/login.vue"
import UserRegister  from  "../views/register.vue"
import Store from "../views/store.vue"
import MyStore from "../views/Seller/myStore.vue"
import SellerRequest from "../views/Seller/request.vue"
import AdminRequest from "../views/Admin/request.vue"
import AdminUserView from "../views/Admin/user.vue"
import Shelf from "../views/shelf.vue"
import Cart from "../views/Buyer/cart.vue"
import RequestRecord from '../views/Seller/requestRecord.vue'
import GoodsRequest from '../views/Admin/goodsRequest.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },{
      path:'/register',
      name:'register',
      component:UserRegister
    },{
      path:'/admin',
      name:'admin',
      children:[
        {
          path:'login',
          name:'adminLogin',
          component:AdminLogin
        },
        {
          path:'index',
          name:'adminHome',
          component:AdminHome,
          redirect:'/admin/index/store',
          children:[
            {
              path:'store',
              component:Store
            },
            {
              path:'shelf',
              component:Shelf

            },
            {
              path:'request',
              component:AdminRequest
            },
            {
              path:'goodsRequest',
              component:GoodsRequest
            },
            {
              path:'user',
              component:AdminUserView
            },
          ]
        }
      ]
    },
    {
      path:'/seller',
      name:'seller',
      children:[
        {
          path:'login',
          name:'sellerLogin',
          component:SellerLogin
        },
        {
          path:'index',
          name:'sellerHome',
          component:SellerHome,
          redirect:'/seller/index/store',
          children:[
            {
              path:'/seller/index/store',
              component:Store
            },
            {
              path:'/seller/index/myStore',
              component:MyStore
            },
            {
              path:'/seller/index/request',
              component:SellerRequest
            },
            {
              path:'/seller/index/shelf',
              component:Shelf

            },
            {
              path:'/seller/index/requestRecord',
              component:RequestRecord
            },
          ]
        }
      ]
    },
    {
      path:'/buyer',
      name:'buyer',
      children:[
        {
          path:'login',
          name:'buyerLogin',
          component:BuyerLogin
        },
        {
          path:'index',
          name:'buyerHome',
          component:BuyerHome,
          redirect:'/buyer/index/store',
          children:[
            {
              path:'/buyer/index/store',
              component:Store
            },
            {
              path:'/buyer/index/shelf',
              component:Shelf

            },
            {
              path:'/buyer/index/cart',
              component:Cart
            }
          ]
        }
      ]
    }
  ]
});

export default router

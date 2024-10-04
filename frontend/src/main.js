import { createApp} from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

 import './assets/main.css'
import axios from 'axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)


const instance = axios.create({
    baseURL: '/api',
    withCredentials:true
});


instance.interceptors.request.use(function (config) {
    const token = window.localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `${token}`
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});
 
instance.interceptors.response.use(function (response) {
    if (response.status === 200) {
        return Promise.resolve(response);
    } else {
        return Promise.reject(response);
    }
}, function (error) {
    if (error.response.status) {
        switch (error.response.status) {                
            case 401:
                router.replace({
                    path: '/buyer/login',
                });
                break;            
            case 403:
                localStorage.removeItem('token');
                setTimeout(() => {
                    router.replace({
                        path: '/buyer/login',
                    });
                }, 1000);
                break;
            case 404:
                break;
            default:
    
        }
        return Promise.reject(error.response);
    }
});

// router.beforeEach((to, from, next) => {
//     const token = window.localStorage.getItem('token');
//     if (to.path==='/register' || to.path === '/admin/login' || to.path === '/seller/login' || to.path === '/buyer/login' || to.path=== '/') {
//         return next();
//     }
//     if (!token) return next('/buyer/login');

//     instance
//       .post("/tokenCheck")
//       .then(function (res) {
//         return next();
//       })
//       .catch(function (error) {
//         return next('/buyer/login')
//       });
    
//   });


app.config.globalProperties.$http=instance;


app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.mount('#app')

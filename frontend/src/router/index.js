import {createRouter, createWebHistory} from "vue-router";


const routes = [
    {
        path: '/',
        component: () => import('@/views/OperationsList.vue'),
        name: 'home',
        props: true,
        meta: {
            requiresAuth: true
        },
    },
    {
        path: '/results/',
        component: () => import('@/views/PredictResults/PredictResults.vue'),
        name: 'predict_results',
        props: true,
        meta: {
            requiresAuth: true
        },
    },
    {
        path: '/tas/:tasId/',
        component: () => import('@/views/TASDetail/TASDetail.vue'),
        name: 'tas_detail',
        props: true,
        meta: {
            requiresAuth: true
        },
    },
    {
        path: '/login',
        component: () => import('@/views/login/Login.vue'),
        name: 'login',
        props: true
    },
    {
        path: '/account',
        component: () => import('@/views/account/AccountInfo.vue'),
        name: 'account',
        meta: {
            requiresAuth: true
        },
        props: true
    },
    {
        path: '/account_edit',
        component: () => import('@/views/account/AccountEdit.vue'),
        name: 'account_edit',
        meta: {
            requiresAuth: true
        }
    },
    // {
    //     path: '/account/password-reset/:uid/:token',
    //     component: () => import('@/views/login/PasswordReset'),
    //     name: 'password_reset',
    //     props: true,
    // },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const user_str = localStorage.getItem('user')
    if (!localStorage.getItem('isAuthenticated')) {
      //TODO: check_auth or getMe method to check auth status
      router.push({name: 'login'})
    } else {
      next()
    }
  } else {
    next()
  }
})

// router.beforeEach((to, from, next) => {
//   if (to.name === "tas_detail" && !to.query.hasOwnProperty("tab")){
//     router.push({name: 'tas_detail', params: {tasId: to.params.tasId}, query: {tab: "1"}})
//   } else {
//     next()
//   }
// })

const originalPush = router.push;
router.push = function push(location) {
  const result = originalPush.call(
      this,
      location,
  );
  if (result) {
    return result.catch(err => {
      if (err.name !== 'NavigationDuplicated') {
        throw err;
      }
    });
  }
  return result;
};


export default router

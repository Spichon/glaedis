import Vue from 'vue';
import Router from 'vue-router';
import {Auth} from 'aws-amplify';
import RouterComponent from './components/RouterComponent.vue';
import {dispatchUserLogIn} from '@/store/main/actions';

Vue.use(Router);

const router =  new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'landingPage',
      component: () => import(
        /* webpackChunkName: "main-accounts-edit" */ './views/Home.vue'),
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import(
        /* webpackChunkName: "main-accounts-edit" */ './views/Auth.vue'),
    },
    {
      path: '/main',
      component: () => import(/* webpackChunkName: "main" */ './views/main/Main.vue'),
      meta: { requiresAuth: true},
      children: [
        {
          path: 'dashboard',
          name: 'main-dashboard',
          component: () => import(/* webpackChunkName: "main-dashboard" */ './views/main/Dashboard.vue'),
        },
        {
          path: 'accounts',
          component: RouterComponent,
          children: [
            {
              path: 'all',
              name: 'main-accounts-all',
              component: () => import(
                /* webpackChunkName: "main-accounts" */ './views/main/account/ListAccounts.vue'),
            },
            {
              path: 'edit/:id',
              name: 'main-accounts-edit',
              component: () => import(
                /* webpackChunkName: "main-accounts-edit" */ './views/main/account/EditAccount.vue'),
            },
            {
              path: 'show/:id',
              name: 'main-accounts-show',
              component: () => import(
                /* webpackChunkName: "main-accounts-show" */ './views/main/account/ShowAccount.vue'),
            },
            {
              path: 'create',
              name: 'main-accounts-create',
              component: () => import(
                /* webpackChunkName: "main-accounts-create" */ './views/main/account/CreateAccount.vue'),
            },
          ],
        },
      ],
    },
    {
      path: '/*', redirect: '/',
    },
  ],
});

router.beforeResolve((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    Auth.currentAuthenticatedUser().then(() => {
      next();
    }).catch(() => {
      next({
        name: 'auth',
      });
    });
  }
  next();
});

export default router;

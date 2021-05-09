import {api} from '../../api';
import router from '../../router';
import {AxiosError} from 'axios';
import {getStoreAccessors} from 'typesafe-vuex';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {
    commitAddNotification,
    commitRemoveNotification,
} from './mutations';
import {AppNotification, MainState} from './state';
import {Auth} from 'aws-amplify';

type MainContext = ActionContext<MainState, State>;

export const actions = {
    async actionUserLogOut(context: MainContext) {
        await dispatchLogOut(context);
        commitAddNotification(context, { content: 'Logged out', color: 'success' });
    },
    async actionUserLogIn(context: MainContext) {
        await dispatchLogIn(context);
        commitAddNotification(context, { content: 'Logged In', color: 'success' });
    },
    async actionLogOut(context: MainContext) {
        await dispatchRemoveLogIn(context);
        await dispatchRouteLogOut(context);
    },
    async actionLogIn(context: MainContext) {
        await dispatchRouteLogIn(context);
    },
    async actionRemoveLogIn() {
        await Auth.signOut();
    },
    actionRouteLogOut() {
        router.push('/');
    },
    actionRouteLogIn() {
        router.push({name: 'main-dashboard'});
    },
    async removeNotification(context: MainContext, payload: { notification: AppNotification, timeout: number }) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                commitRemoveNotification(context, payload.notification);
                resolve(true);
            }, payload.timeout);
        });
    },
};

const {dispatch} = getStoreAccessors<MainState | any, State>('');

export const dispatchRemoveNotification = dispatch(actions.removeNotification);
export const dispatchRouteLogOut = dispatch(actions.actionRouteLogOut);
export const dispatchRouteLogIn = dispatch(actions.actionRouteLogIn);
export const dispatchRemoveLogIn = dispatch(actions.actionRemoveLogIn);
export const dispatchUserLogOut = dispatch(actions.actionUserLogOut);
export const dispatchUserLogIn = dispatch(actions.actionUserLogIn);
export const dispatchLogOut = dispatch(actions.actionLogOut);
export const dispatchLogIn = dispatch(actions.actionLogIn);


import {api} from '../../api';
import {ActionContext} from 'vuex';
import {IAccountCreate, IAccountUpdate} from '../../interfaces';
import {State} from '../state';
import {AccountState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetAccounts, commitSetAccount, commitRemoveAccount} from './mutations';
import {commitAddNotification, commitRemoveNotification} from '@/store/main/mutations';

type MainContext = ActionContext<AccountState, State>;

export const actions = {
    async actionGetAccounts(context: MainContext) {
        try {
            const response = await api.getAccounts();
            if (response) {
                commitSetAccounts(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionUpdateAccount(context: MainContext, payload: { id: number, account: IAccountUpdate }) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateAccount(payload.id, payload.account),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetAccount(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Account successfully updated', color: 'success'});
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionCreateAccount(context: MainContext, payload: IAccountCreate) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createAccount(payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Account successfully created', color: 'success'});
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
    async actionDeleteAccount(context: MainContext, payload: { id: number }) {
        try {
            const loadingNotification = {content: 'saving', showProgress: true};
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteAccount(payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveAccount(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, {content: 'Account successfully Deleted', color: 'success'});
        } catch (error) {
           const errorNotification = {content: error, showProgress: false};
           commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<AccountState, State>('');

export const dispatchCreateAccount = dispatch(actions.actionCreateAccount);
export const dispatchGetAccounts = dispatch(actions.actionGetAccounts);
export const dispatchUpdateAccount = dispatch(actions.actionUpdateAccount);
export const dispatchDeleteAccount = dispatch(actions.actionDeleteAccount);

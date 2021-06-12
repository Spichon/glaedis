import {api} from '../../api';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {TransactionState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetTransactions} from './mutations';
import {commitAddNotification} from '@/store/main/mutations';

type MainContext = ActionContext<TransactionState, State>;

export const actions = {
    async actionGetTransactions(context: MainContext, payload: { id: number }) {
        try {
            const response = await api.getTransactions(payload.id);
            if (response) {
                commitSetTransactions(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<TransactionState, State>('');

export const dispatchGetTransactions = dispatch(actions.actionGetTransactions);

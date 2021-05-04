import {api} from '../../api';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {BrokerState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetBrokers} from './mutations';
import {commitAddNotification} from '@/store/main/mutations';

type MainContext = ActionContext<BrokerState, State>;

export const actions = {
    async actionGetBrokers(context: MainContext) {
        try {
            const response = await api.getBrokers();
            if (response) {
                commitSetBrokers(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<BrokerState, State>('');

export const dispatchGetBrokers = dispatch(actions.actionGetBrokers);

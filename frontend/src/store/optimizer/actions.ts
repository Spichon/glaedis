import {api} from '../../api';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {OptimizerState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetOptimizers} from './mutations';
import {commitAddNotification} from '@/store/main/mutations';

type MainContext = ActionContext<OptimizerState, State>;

export const actions = {
    async actionGetOptimizers(context: MainContext) {
        try {
            const response = await api.getOptimizers();
            if (response) {
                commitSetOptimizers(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<OptimizerState, State>('');

export const dispatchGetOptimizers = dispatch(actions.actionGetOptimizers);

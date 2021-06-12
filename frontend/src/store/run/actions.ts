import {api} from '../../api';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {RunState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {commitSetRuns} from './mutations';
import {commitAddNotification} from '@/store/main/mutations';
import {commitSetPortfolios} from "@/store/portfolio/mutations";

type MainContext = ActionContext<RunState, State>;

export const actions = {
    async actionGetRuns(context: MainContext, payload: { id: number }) {
        try {
            const response = await api.getRuns(payload.id);
            if (response) {
                commitSetRuns(context, response.data);
            }
        } catch (error) {
            const errorNotification = {content: error, showProgress: false};
            commitAddNotification(context, errorNotification);
        }
    },
};

const {dispatch} = getStoreAccessors<RunState, State>('');

export const dispatchGetRuns = dispatch(actions.actionGetRuns);

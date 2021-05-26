import {IAccount, IBroker} from '../../interfaces';
import {BrokerState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const mutations = {
    setBrokers(state: BrokerState, payload: IBroker[]) {
        state.brokers = payload;
    },
};

const {commit} = getStoreAccessors<BrokerState, State>('');

export const commitSetBrokers = commit(mutations.setBrokers);


import { BrokerState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    brokers: (state: BrokerState) => state.brokers,
    oneBroker: (state: BrokerState) => (brokerId: number) => {
        const filteredBrokers = state.brokers.filter((broker) => broker.id === brokerId);
        if (filteredBrokers.length > 0) {
            return { ...filteredBrokers[0] };
        }
    },
};

const { read } = getStoreAccessors<BrokerState, State>('');

export const readOneBroker = read(getters.oneBroker);
export const readBrokers = read(getters.brokers);

import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import {BrokerState} from './state';

const defaultState: BrokerState = {
  brokers: [],
};

export const brokerModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};

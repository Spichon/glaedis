import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import {TransactionState} from './state';

const defaultState: TransactionState = {
  transactions: [],
};

export const transactionModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};

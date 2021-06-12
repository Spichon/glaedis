import { TransactionState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    transactions: (state: TransactionState) => state.transactions,
    oneTransaction: (state: TransactionState) => (transactionId: number) => {
        const filteredTransactions = state.transactions.filter((transaction) => transaction.id === transactionId);
        if (filteredTransactions.length > 0) {
            return { ...filteredTransactions[0] };
        }
    },
};

const { read } = getStoreAccessors<TransactionState, State>('');

export const readOneTransaction = read(getters.oneTransaction);
export const readTransactions = read(getters.transactions);

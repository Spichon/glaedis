import { PortfolioState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    portfolios: (state: PortfolioState) => state.portfolios,
    onePortfolio: (state: PortfolioState) => (portfolioId: number) => {
        const filteredUsers = state.portfolios.filter((portfolio) => portfolio.id === portfolioId);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
};

const { read } = getStoreAccessors<PortfolioState, State>('');

export const readOnePortfolio = read(getters.onePortfolio);
export const readPortfolios = read(getters.portfolios);

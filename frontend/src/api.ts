import axios from 'axios';
import {apiUrl} from './env';
import {Auth} from 'aws-amplify';
import {
    IUserProfile,
    IAccount, IAccountUpdate, IAccountCreate,
    IBroker,
    IPortfolio, IPortfolioCreate, IPortfolioUpdate,
    IOptimizer,
    IRun,
    ITransaction
} from './interfaces';

async function authHeaders() {
    return {
        headers: {
            Authorization: `Bearer ${(await Auth.currentSession()).getAccessToken().getJwtToken()}`,
        },
    };
}

export const api = {
    async getMe() {
        return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, await authHeaders());
    },
    async getAccounts() {
        return axios.get<IAccount[]>(`${apiUrl}/api/v1/accounts/`, await authHeaders());
    },
    async updateAccount(accountId: number, data: IAccountUpdate) {
        return axios.put(`${apiUrl}/api/v1/accounts/${accountId}`, data, await authHeaders());
    },
    async createAccount(data: IAccountCreate) {
        return axios.post(`${apiUrl}/api/v1/accounts/`, data, await authHeaders());
    },
    async deleteAccount(accountId: number) {
        return axios.delete(`${apiUrl}/api/v1/accounts/${accountId}`, await authHeaders());
    },
    async getBrokers() {
        return axios.get<IBroker[]>(`${apiUrl}/api/v1/brokers/`, await authHeaders());
    },
    async getAvailableAssets(brokerId: number) {
        return axios.get(`${apiUrl}/api/v1/brokers/${brokerId}/available_assets`, await authHeaders());
    },
    async getQuoteAssets(brokerId: number) {
        return axios.get(`${apiUrl}/api/v1/brokers/${brokerId}/quote_assets`, await authHeaders());
    },
    async getTradableAssetPairs(assetBrokerId: number) {
        return axios.get(`${apiUrl}/api/v1/brokers/${assetBrokerId}/tradable_asset_pairs`, await authHeaders());
    },
    async getTimeframes(brokerId: number) {
        return axios.get(`${apiUrl}/api/v1/brokers/${brokerId}/get_timeframes`, await authHeaders());
    },
    async getPortfolios() {
        return axios.get<IPortfolio[]>(`${apiUrl}/api/v1/portfolios/`, await authHeaders());
    },
    async updatePortfolio(portfolioId: number, data: IPortfolioUpdate) {
        return axios.put(`${apiUrl}/api/v1/portfolios/${portfolioId}`, data, await authHeaders());
    },
    async createPortfolio(data: IPortfolioCreate) {
        return axios.post(`${apiUrl}/api/v1/portfolios/`, data, await authHeaders());
    },
    async deletePortfolio(portfolioId: number) {
        return axios.delete(`${apiUrl}/api/v1/portfolios/${portfolioId}`, await authHeaders());
    },
    // async startAutomation(token: string, portfolioId: number) {
    //     return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/start_automation`, authHeaders(token));
    // },
    // async pauseAutomation(token: string, portfolioId: number) {
    //     return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/pause_automation`, authHeaders(token));
    // },
    // async deleteAutomation(token: string, portfolioId: number) {
    //     return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/delete_automation`, authHeaders(token));
    // },
    async getPortfolioEquityBalance(portfolioId: number) {
        return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/get_portfolio_equity_balance`, await authHeaders());
    },
    async getPortfolioAssets(portfolioId: number) {
        return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/get_portfolio_assets`, await authHeaders());
    },
    async getOptimizers() {
        return axios.get<IOptimizer[]>(`${apiUrl}/api/v1/optimizers`, await authHeaders());
    },
    async getRuns(portfolioId: number) {
        return axios.get<IRun[]>(`${apiUrl}/api/v1/runs/${portfolioId}`, await authHeaders());
    },
    async getTransactions(portfolioId: number) {
        return axios.get<ITransaction[]>(`${apiUrl}/api/v1/transactions/${portfolioId}`, await authHeaders());
    },
};

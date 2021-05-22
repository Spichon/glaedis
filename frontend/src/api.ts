import axios from 'axios';
import {apiUrl} from './env';
import {Auth} from 'aws-amplify';
import {
    IUserProfile,
    IAccount, IAccountUpdate, IAccountCreate,
    IBroker,
    IPortfolio, IPortfolioCreate, IPortfolioUpdate,
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
    async getPortfolios() {
        return axios.get<IPortfolio[]>(`${apiUrl}/api/v1/portfolios/`, await authHeaders());
    },
    async getAssetsLastValues(portfolioId: number) {
        return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/get_assets_last_values`, await authHeaders());
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
    async getQuoteAssetBalance(portfolioId: number) {
        return axios.get(`${apiUrl}/api/v1/portfolios/${portfolioId}/get_quote_asset_balance`, await authHeaders());
    },
};

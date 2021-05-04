import axios from 'axios';
import {apiUrl} from './env';
import {Auth} from 'aws-amplify';
import {
    IUserProfile,
    IAccount, IAccountUpdate, IAccountCreate,
    IBroker,
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
};

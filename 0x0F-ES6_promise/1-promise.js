export default function getResponseFromAPI(success) {
    if (!success) return Promise.reject(new Error('The fake API is not working currently'));
    return Promise.resolve({
        status: 200,
        body: 'success',
    });
}
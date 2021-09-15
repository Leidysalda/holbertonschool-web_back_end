<<<<<<< HEAD
export default function handleResponseFromAPI(promise) {
    return promise
    .then(() => ({ 
        status: 200,
        body: 'success'
    }))
    .catch(() => new Error())
    .finally(() => console.log('Got a response from the API'))
=======
export default function handleResponseFromAPI(promise) {
    return promise
    .then(() => ({ 
        status: 200,
        body: 'success'
    }))
    .catch(() => new Error())
    .finally(() => console.log('Got a response from the API'))
>>>>>>> e9fd4fef0a7a0de51270adc075d0102bf18bd12a
}
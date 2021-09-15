<<<<<<< HEAD
export default function loadBalancer(chinaDownload, USDownload) {
    return Promise.race([chinaDownload, USDownload])
    .then((val) => val );
=======
export default function loadBalancer(chinaDownload, USDownload) {
    return Promise.race([chinaDownload, USDownload])
    .then((val) => val );
>>>>>>> e9fd4fef0a7a0de51270adc075d0102bf18bd12a
}
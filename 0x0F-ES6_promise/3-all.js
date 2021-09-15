<<<<<<< HEAD
import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
    return Promise.all([createUser(), uploadPhoto()])
    .then((values) => {
        const [user, photo] = values;
        console.log(`${photo.body} ${user.firstName} ${user.lastname}`);
    })
    .catch(() => console.log('Signup system offline'))
}
=======
import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
    return Promise.all([createUser(), uploadPhoto()])
    .then((values) => {
        const [user, photo] = values;
        console.log(`${photo.body} ${user.firstName} ${user.lastname}`);
    })
    .catch(() => console.log('Signup system offline'))
}
>>>>>>> e9fd4fef0a7a0de51270adc075d0102bf18bd12a

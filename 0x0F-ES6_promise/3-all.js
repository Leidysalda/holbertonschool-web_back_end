import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
    return Promise.all([createUser(), uploadPhoto()])
    .then((values) => {
        const [user, photo] = values;
        console.log(`${photo.body} ${user.firstName} ${user.lastname}`);
    })
    .catch(() => console.log('Signup system offline'))
}

import { createUser, uploadPhoto } from './utils';

export default function asyncUploadUser() {
    try {
        const user = await createUser();
        const photo = await uploadPhoto();
        return {
            photo,
            user,
        };
    } catch (err) {
        return {
            photo: null,
            user: null,
        };
    }
}
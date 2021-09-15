<<<<<<< HEAD
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
=======
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
>>>>>>> e9fd4fef0a7a0de51270adc075d0102bf18bd12a
}
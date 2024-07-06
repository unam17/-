// src/components/SocialLogin.js
import React, { useState } from 'react';
import axios from 'axios';

const SocialLogin = () => {
    const [userInfo, setUserInfo] = useState(null);

    const handleLogin = async (provider) => {
        const loginUrl = `http://localhost:8000/accounts/${provider}/login/`;

        const newWindow = window.open(loginUrl, '_blank', 'width=600,height=400');

        const interval = setInterval(() => {
            if (newWindow.closed) {
                clearInterval(interval);
                // 로그인 성공 후 처리
                axios.get('http://localhost:8000/api/auth/user/')
                    .then(response => {
                        console.log('User data:', response.data);
                        localStorage.setItem('token', response.data.token);
                        fetchUserProfile();
                    })
                    .catch(error => {
                        console.error('Error fetching user data:', error);
                    });
            }
        }, 500);
    };

    const fetchUserProfile = () => {
        const token = localStorage.getItem('token');
        axios.get('http://localhost:8000/accounts/profile/', {
            headers: {
                Authorization: `Token ${token}`,
            },
        })
        .then(response => {
            setUserInfo(response.data);
        })
        .catch(error => {
            console.error('Error fetching user profile:', error);
        });
    };

    return (
        <div>
            <button onClick={() => handleLogin('google')}>Login with Google</button>
            <button onClick={() => handleLogin('kakao')}>Login with Kakao</button>
            <button onClick={() => handleLogin('naver')}>Login with Naver</button>
            {userInfo && (
                <div>
                    <h2>User Information</h2>
                    <p>Name: {userInfo.username}</p>
                    <p>Email: {userInfo.email}</p>
                    <p>Phone Number: {userInfo.phone_number}</p>
                </div>
            )}
        </div>
    );
};

export default SocialLogin;


import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [bio, setBio] = useState('');

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const response = await axios.get('/profile');
        setUser(response.data);
        setBio(response.data.bio);
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    };
    fetchUserProfile();
  }, []);

  const handleEditProfile = () => {
    setEditMode(true);
  };

  const handleSaveProfile = async () => {
    try {
      await axios.put('/profile', { bio });
      setUser((prevUser) => ({ ...prevUser, bio }));
      setEditMode(false);
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div>
        {user.profile_picture ? (
          <img src={user.profile_picture} alt="Profile" />
        ) : (
          <div>No profile picture</div>
        )}
      </div>
      <h2>{user.username}</h2>
      <p>{user.email}</p>
      {editMode ? (
        <div>
          <textarea value={bio} onChange={(e) => setBio(e.target.value)} />
          <button onClick={handleSaveProfile}>Save</button>
        </div>
      ) : (
        <div>
          <p>{user.bio}</p>
          <button onClick={handleEditProfile}>Edit Profile</button>
        </div>
      )}
    </div>
  );
};

export default Profile;

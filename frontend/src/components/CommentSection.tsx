import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Comment {
  id: number;
  text: string;
  created_at: string;
}

interface Props {
  photoId: number;
}

const CommentSection: React.FC<Props> = ({ photoId }) => {
  const [comments, setComments] = useState<Comment[]>([]);
  const [newComment, setNewComment] = useState<string>('');

  useEffect(() => {
    const fetchComments = async () => {
      try {
        const response = await axios.get(`/api/comments/?photo=${photoId}`);
        setComments(response.data);
      } catch (error) {
        console.error('Error fetching comments:', error);
      }
    };

    fetchComments();
  }, [photoId]);

  const handleAddComment = async () => {
    try {
      const response = await axios.post('/api/comments/', {
        text: newComment,
        photo: photoId,
      });
      setComments([...comments, response.data]);
      setNewComment('');
    } catch (error) {
      console.error('Error adding comment:', error);
    }
  };

  return (
    <div>
      <h3>Comments</h3>
      <div>
        {comments.map(comment => (
          <div key={comment.id}>
            <p>{comment.text}</p>
            <small>{new Date(comment.created_at).toLocaleString()}</small>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={newComment}
        onChange={e => setNewComment(e.target.value)}
        placeholder="Add a comment"
      />
      <button onClick={handleAddComment}>Add Comment</button>
    </div>
  );
};

export default CommentSection;
import React, { useState } from 'react';

const EmojiTicTacToe = () => {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [currentPlayer, setCurrentPlayer] = useState('🟢');
  const [winner, setWinner] = useState(null);

  const handleClick = (index) => {
    if (board[index] === null && winner === null) {
      const newBoard = [...board];
      newBoard[index] = currentPlayer;
      setBoard(newBoard);
      setCurrentPlayer(currentPlayer === '🟢' ? '🔴' : '🟢');

      // Check for a winner
      const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
      ];
      for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
          setWinner(board[a]);
          return;
        }
      }

      // Check for a tie
      if (!board.includes(null)) {
        setWinner('Tie');
      }
    }
  };

  const handleReset = () => {
    setBoard(Array(9).fill(null));
    setCurrentPlayer('🟢');
    setWinner(null);
  };

  const renderSquare = (index) => (
    <div
      className="square"
      onClick={() => handleClick(index)}
      style={{
        width: '100px',
        height: '100px',
        border: '1px solid black',
        display: 'inline-block',
        fontSize: '50px',
        textAlign: 'center',
        lineHeight: '100px',
        cursor: 'pointer',
        backgroundColor: board[index] === '🟢' ? 'lightgreen' : board[index] === '🔴' ? 'lightcoral' : 'white',
      }}
    >
      {board[index]}
    </div>
  );

  return (
    <div>
      <h1>Emoji Tic Tac Toe</h1>
      <div>
        {[0, 1, 2].map((row) => (
          <div key={row}>
            {[0, 1, 2].map((col) => renderSquare(row * 3 + col))}
          </div>
        ))}
      </div>
      <p>Current Player: {currentPlayer}</p>
      {winner && (
        <div>
          <p>Winner: {winner}</p>
          <button onClick={handleReset}>Reset</button>
        </div>
      )}
    </div>
  );
};

export default EmojiTicTacToe;
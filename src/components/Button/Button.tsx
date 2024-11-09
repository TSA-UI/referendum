// components/Button.tsx
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  type?: 'button' | 'submit' | 'reset';
  variant?: 'primary' | 'secondary' | 'tertiary';
  icon?: React.ReactNode; // Prop untuk ikon
}

const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  disabled = false,
  type = 'button',
  variant = 'primary',
  icon,
}) => {
  const buttonClass = `${styles.button} ${
    variant === 'primary'
      ? styles.primary
      : variant === 'secondary'
      ? styles.secondary
      : styles.tertiary
  }`;

  return (
    <button
      className={buttonClass}
      onClick={onClick}
      disabled={disabled}
      type={type}
    >
      {icon && <span className={styles.icon}>{icon}</span>} {/* Ikon di kiri */}
      {children}
      {icon && <span className={styles.icon}>{icon}</span>} {/* Ikon di kanan */}
    </button>
  );
};

export default Button;

import React from 'react';
import styles from '@/components/Hero/Hero.module.css'
export default function Hero() {
  return (
    <section className={styles.hero}>
      <div className={styles.logo}>
        <img src="/logo.png" alt="Referendum Logo" width="150" height="75" />
      </div>
    </section>
  );
}

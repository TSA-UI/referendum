// components/WhatIsReferendum.tsx
import React from 'react';
import styles from './WhatIsReferendum.module.css';


export default function WhatIsReferendum() {
  return (
    <section className={styles.container}>
        <h2 className={`${styles.title} h2-style`}>What is Referendum?</h2>
        <p className={`${styles.description} p2-style`}>
            <strong>Referendum</strong> adalah sebuah proyek internal TSA UI 2024 dengan serangkaian kegiatan yang dilaksanakan untuk <strong>menentukan President-Vice President TSA Universitas Indonesia terpilih periode 2025</strong> sebagai <strong>langkah awal regenerasi kepemimpinan Management Team TSA UI</strong>.
        </p>
    </section>
  );
}

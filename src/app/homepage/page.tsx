import React from 'react'
import Hero from '@/components/Hero/Hero'
import Timeline from '@/components/Timeline/Timeline'
import WhatIsReferendum from '@/components/WhatIsReferendum/WhatIsReferendum';
import Image from 'next/image';
import CTACard from '@/components/CTACard/CTACard';

export default function page() {
  return (
    <main>
        <Hero />
        <WhatIsReferendum />
        <Timeline />
        <CTACard />
    </main>
    
  )
}

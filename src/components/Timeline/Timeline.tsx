// components/home/Timeline.tsx
export default function Timeline() {
    const events = [
      {
        title: "Pendaftaran Paslon",
        date: "27 Okt - 2 Nov 2024",
      },
      {
        title: "Online Briefing Paslon",
        date: "4 November 2024",
      },
      // ... tambahkan event lainnya
    ];
  
    return (
      <section className="py-16 bg-emerald-50">
        <h2 className="text-3xl text-center mb-12">Our Timeline</h2>
        <div className="container mx-auto px-4">
          <div className="relative">
            {/* Timeline line */}
            <div className="absolute w-full h-1 bg-emerald-200 top-1/2 -translate-y-1/2" />
            
            {/* Timeline events */}
            <div className="relative grid grid-cols-1 md:grid-cols-3 gap-8">
              {events.map((event, index) => (
                <div key={index} className="bg-white p-6 rounded-lg shadow-md">
                  <h3 className="font-bold mb-2">{event.title}</h3>
                  <p className="text-gray-600">{event.date}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    );
  }
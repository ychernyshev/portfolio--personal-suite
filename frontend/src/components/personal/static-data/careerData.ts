export interface CareerItem {
    id: string;
    date: string;
    title: string;
    type: 'work' | 'education' | 'other';
    currentOccupation: string;
    occupationDescription: string,
    description: string;
    techStack?: string[];
    projects?: project[];
}

interface project {
    title: string
    description: string
    livePreviewUrl: string
    sourceCodeUrl?: string
}

export const timeline: CareerItem[] = [
    {
        id: 'exp-2025',
        date: 'october 2025 - Present',
        title: 'Expanding and deepening skills',
        type: 'work',
        currentOccupation: 'Head of the post office',
        description: 'Currently focusing on building personal brand ecosystem "Code & Vision". Engineering complex reactive interfaces and robust backends.',
        techStack: ['js', 'python', 'django', 'vue', 'typescript'],
        projects: [
            {
                title: 'Solar Power Calculator',
                description: 'Developed a high-performance analytical dashboard for monitoring solar energy production and cost-efficiency. Engineered complex mathematical engines to calculate energy yield forecasts and financial savings. Integrated dynamic charts and data tables to provide deep insight into energy consumption patterns. Built with a "pixel-perfect" approach, ensuring a seamless user experience across data entry, export, and visual analysis modules.',
                livePreviewUrl: '',
                sourceCodeUrl: 'https://github.com/ychernyshev/portfolio--personal-suite/tree/main/backend/calculator',
            },
            {
                title: 'Post Flow Controlling App (v2.0)',
                description: 'A complete re-engineering of the legacy system into a high-performance Fullstack application. Features a reactive Vue.js frontend and a distributed backend powered by Celery, Redis, and Docker for scalable logistics management.',
                livePreviewUrl: '',
                sourceCodeUrl: '',
            },
        ]
    },
    {
        id: 'exp-2022',
        date: 'september 2022 - september 2025',
        title: 'skill expansion',
        type: 'education',
        currentOccupation: 'Postal Service Worker',
        occupationDescription: 'Responsible for timely delivery and logistics management within a designated area',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python', 'django', 'vue'],
        projects: [
            {
                title: 'Mail & Inventory Internal Tracking System (v1.0)',
                description: 'Developed a custom Lightweight CRM to automate package tracking and subscription management. Implemented custom business logic for automatic expiration tracking and efficient mail archiving. The application replaced manual record-keeping with a searchable database for tracking numbers, recipient data, and newspaper subscriptions, significantly reducing information retrieval time.\'',
                livePreviewUrl: '',
                sourceCodeUrl: '',
            }
        ]
    },
    {
        id: 'exp-2020',
        date: 'august 2020 - february 2022',
        title: 'Skill expansion',
        type: 'education',
        currentOccupation: 'Senior Contact Center Operator',
        occupationDescription: 'Streamlined business processes to enhance client interactions and operational efficiency. Regularly resolved unique, high-stakes inquiries while identifying opportunities for system improvements. As a Senior Specialist, I managed complex cases, maintained databases, and developed training documentation.',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python', 'django'],
        projects: [
            {
                title: '',
                description: '',
                livePreviewUrl: '',
                sourceCodeUrl: '',
            }
        ]
    },
    {
        id: 'exp-2018',
        date: 'march 2018 - april 2020',
        title: 'Started',
        type: 'work',
        currentOccupation: 'Contact Center Specialist',
        occupationDescription: 'Focused on resolving high-complexity tasks and optimizing internal database processes. Actively mentored new team members and authored technical guidelines to improve overall call center performance.',
        description: 'Mastered 10+ projects...',
        techStack: ['html', 'css'],
        projects: [
            {
                title: 'static page: focus on semantic HTML & CSS',
                description: 'The tool was used as a cheat sheet during a work session. This tool collected and organized information in a single window for easy navigation. The updated tool was sent via work email.',
                livePreviewUrl: 'oriflame-tool',
            }
        ]
    },
];
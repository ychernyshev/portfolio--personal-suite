export interface CareerItem {
    id: string;
    date: string;
    title: string;
    type: 'work' | 'education' | 'other';
    currentOccupation: string;
    description: string;
    techStack?: string[];
}

export const timeline: CareerItem[] = [
    {
        id: 'exp-2025',
        date: 'october 2025 - Present',
        title: 'Full-Stack Developer',
        type: 'work',
        currentOccupation: 'Head of the post office',
        description: 'Currently focusing on building personal brand ecosystem "Code & Vision". Engineering complex reactive interfaces and robust backends.',
        techStack: ['vue', 'typescript', 'django'],
    },
    {
        id: 'exp-2022',
        date: 'september 2022 - september 2025',
        title: 'Study & Research',
        type: 'education',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python'],
    },
    {
        id: 'exp-2020',
        date: 'august 2020 - february 2022',
        title: 'Study & Research',
        type: 'education',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python'],
    },
    {
        id: 'exp-2018',
        date: 'march 2018 - april 2020',
        title: 'Study & Research',
        type: 'education',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python'],
    },
    {
        id: 'exp-2016',
        date: 'november 2016 - november 2016',
        title: 'Study & Research',
        type: 'education',
        description: 'Mastered 10+ projects...',
        techStack: ['js', 'python'],
    },
];
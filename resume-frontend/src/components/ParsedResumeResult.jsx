import { motion } from "framer-motion";
import {
    Award,
    BadgeCheck,
    Briefcase,
    TrendingUp,
    User,
    Zap,
} from "lucide-react";

// ✨ Animated Circular Progress Bar Component
const CircularProgress = ({ score, maxScore = 10 }) => {
  const radius = 45;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (score / maxScore) * circumference;
  const percentage = (score / maxScore) * 100;

  // Color based on score
  let color = "#ef4444"; // red
  if (percentage >= 70) color = "#22c55e"; // green
  else if (percentage >= 50) color = "#f59e0b"; // amber

  return (
    <motion.svg
      width="140"
      height="140"
      className="drop-shadow-lg"
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.6, delay: 0.3 }}
    >
      {/* Background circle */}
      <circle
        cx="70"
        cy="70"
        r={radius}
        fill="none"
        stroke="#e2e8f0"
        strokeWidth="6"
      />

      {/* Animated progress circle */}
      <motion.circle
        cx="70"
        cy="70"
        r={radius}
        fill="none"
        stroke={color}
        strokeWidth="6"
        strokeDasharray={circumference}
        initial={{ strokeDashoffset: circumference }}
        animate={{ strokeDashoffset }}
        transition={{ duration: 1, delay: 0.5, ease: "easeOut" }}
        strokeLinecap="round"
      />

      {/* Score text */}
      <text
        x="70"
        y="75"
        textAnchor="middle"
        fontSize="32"
        fontWeight="bold"
        fill="#1e293b"
        className="font-inter"
      >
        {score}
      </text>
      <text
        x="70"
        y="95"
        textAnchor="middle"
        fontSize="12"
        fill="#94a3b8"
        className="font-inter"
      >
        / {maxScore}
      </text>
    </motion.svg>
  );
};

// ✨ Animated Skill Badge Component
const SkillBadge = ({ skill, index }) => {
  const colors = [
    "from-blue-400 to-blue-600",
    "from-indigo-400 to-indigo-600",
    "from-purple-400 to-purple-600",
    "from-cyan-400 to-cyan-600",
    "from-teal-400 to-teal-600",
    "from-slate-400 to-slate-600",
  ];

  const colorClass = colors[index % colors.length];

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8, y: 10 }}
      animate={{ opacity: 1, scale: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.1 * index }}
      whileHover={{ scale: 1.08, y: -3 }}
      className={`
        px-4 py-2 rounded-full 
        bg-gradient-to-r ${colorClass}
        text-white text-sm font-semibold
        shadow-md hover:shadow-lg
        transition-shadow duration-300
        cursor-default
        backdrop-blur-sm
      `}
    >
      {skill}
    </motion.div>
  );
};

// ✨ Main ParsedResumeResult Component
const ParsedResumeResult = ({ data }) => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.2,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.5, ease: "easeOut" },
    },
  };

  return (
    <motion.div
      className="w-full max-w-3xl mx-auto px-4 py-8"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      {/* Main Premium Card Container */}
      <motion.div
        className="
          relative rounded-3xl 
          bg-white 
          border border-slate-200
          shadow-2xl
          overflow-hidden
        "
        variants={itemVariants}
      >
        {/* Decorative gradient background */}
        <div className="absolute inset-0 bg-gradient-to-br from-blue-50 via-white to-indigo-50 opacity-60 pointer-events-none" />

        <div className="relative z-10 p-8 md:p-10">
          {/* ========== HEADER SECTION ========== */}
          <motion.div className="text-center mb-10" variants={itemVariants}>
            <motion.div
              className="flex justify-center mb-6"
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ duration: 0.5, delay: 0.1 }}
            >
              <div className="w-16 h-16 bg-gradient-to-br from-blue-400 to-indigo-600 rounded-full flex items-center justify-center shadow-lg">
                <User className="w-8 h-8 text-white" />
              </div>
            </motion.div>

            <motion.h1
              className="text-4xl md:text-5xl font-bold text-slate-900 mb-2"
              variants={itemVariants}
            >
              {data.name}
            </motion.h1>

            <motion.div
              className="flex items-center justify-center gap-2 text-indigo-600 font-medium"
              variants={itemVariants}
            >
              <BadgeCheck className="w-5 h-5" />
              <span>AI Resume Analysis</span>
            </motion.div>
          </motion.div>

          {/* ========== MAIN STATS GRID ========== */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
            {/* Fit Score Card */}
            <motion.div
              className="
                col-span-1 md:col-span-1
                flex flex-col items-center justify-center
                p-6 rounded-2xl
                bg-gradient-to-br from-blue-50 to-indigo-50
                border border-blue-200
                hover:shadow-lg transition-all duration-300
              "
              variants={itemVariants}
              whileHover={{ y: -5 }}
            >
              <p className="text-sm font-semibold text-slate-600 mb-4 uppercase tracking-wider">
                Fit Score
              </p>
              <CircularProgress score={data.fit_score} maxScore={10} />
              <motion.div
                className="mt-4 text-center"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1 }}
              >
                <p className="text-xs text-slate-500 mt-2">
                  {data.fit_score >= 8
                    ? "Excellent Match"
                    : data.fit_score >= 6
                      ? "Strong Candidate"
                      : "Potential Candidate"}
                </p>
              </motion.div>
            </motion.div>

            {/* Experience Card */}
            <motion.div
              className="
                col-span-1 md:col-span-1
                flex flex-col items-center justify-center
                p-6 rounded-2xl
                bg-gradient-to-br from-purple-50 to-pink-50
                border border-purple-200
                hover:shadow-lg transition-all duration-300
              "
              variants={itemVariants}
              whileHover={{ y: -5 }}
            >
              <Briefcase className="w-8 h-8 text-purple-600 mb-3" />
              <p className="text-sm font-semibold text-slate-600 mb-3 uppercase tracking-wider">
                Experience
              </p>
              <motion.div
                className="text-3xl font-bold text-purple-600"
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.6, delay: 0.4 }}
              >
                {data.experience}
              </motion.div>
              <p className="text-sm text-slate-500 mt-2">
                {data.experience === 1 ? "Year" : "Years"}
              </p>
            </motion.div>

            {/* Tech Count Card */}
            <motion.div
              className="
                col-span-1 md:col-span-1
                flex flex-col items-center justify-center
                p-6 rounded-2xl
                bg-gradient-to-br from-amber-50 to-orange-50
                border border-amber-200
                hover:shadow-lg transition-all duration-300
              "
              variants={itemVariants}
              whileHover={{ y: -5 }}
            >
              <Zap className="w-8 h-8 text-amber-600 mb-3" />
              <p className="text-sm font-semibold text-slate-600 mb-3 uppercase tracking-wider">
                Skills
              </p>
              <motion.div
                className="text-3xl font-bold text-amber-600"
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.6, delay: 0.5 }}
              >
                {data.tech_stack?.length || 0}
              </motion.div>
              <p className="text-sm text-slate-500 mt-2">Technologies</p>
            </motion.div>
          </div>

          {/* ========== TECH STACK SECTION ========== */}
          {data.tech_stack && data.tech_stack.length > 0 && (
            <motion.div variants={itemVariants}>
              <motion.div
                className="mb-4 flex items-center gap-2"
                variants={itemVariants}
              >
                <Award className="w-5 h-5 text-indigo-600" />
                <h2 className="text-lg font-bold text-slate-900">
                  Technical Skills
                </h2>
              </motion.div>

              <motion.div
                className="
                  flex flex-wrap gap-3
                  p-6 rounded-2xl
                  bg-slate-50 border border-slate-200
                "
                variants={containerVariants}
              >
                {data.tech_stack.map((skill, index) => (
                  <SkillBadge key={`${skill}-${index}`} skill={skill} index={index} />
                ))}
              </motion.div>
            </motion.div>
          )}

          {/* ========== FOOTER CTA ========== */}
          <motion.div
            className="
              mt-8 p-6 rounded-2xl
              bg-gradient-to-r from-blue-600 to-indigo-600
              text-white text-center
              shadow-lg
            "
            variants={itemVariants}
            whileHover={{ scale: 1.02 }}
          >
            <motion.div
              className="flex items-center justify-center gap-2 mb-2"
              variants={itemVariants}
            >
              <TrendingUp className="w-5 h-5" />
              <p className="font-semibold">Ready for Next Steps?</p>
            </motion.div>
            <p className="text-sm text-blue-100">
              Review the analysis above and proceed with your application.
            </p>
          </motion.div>
        </div>
      </motion.div>
    </motion.div>
  );
};

export default ParsedResumeResult;

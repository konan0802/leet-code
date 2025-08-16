-- https://leetcode.com/problems/students-and-examinations/

WITH AggExaminations AS (
    SELECT
        student_id,
        subject_name,
        COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
)
SELECT
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    ifnull(AggExaminations.attended_exams, 0) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN AggExaminations 
  ON Students.student_id = AggExaminations.student_id
 AND Subjects.subject_name = AggExaminations.subject_name
ORDER BY Students.student_id, Subjects.subject_name

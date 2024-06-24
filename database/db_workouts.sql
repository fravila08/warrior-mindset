CREATE TABLE "Set"(
    "id" UUID NOT NULL,
    "exercise" UUID NOT NULL,
    "weight" INTEGER NOT NULL,
    "reps" BIGINT NOT NULL
);
ALTER TABLE
    "Set" ADD PRIMARY KEY("id");
CREATE TABLE "Muscle_Group"(
    "id" UUID NOT NULL,
    "muscle" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Muscle_Group" ADD PRIMARY KEY("id");
CREATE TABLE "User"(
    "id" UUID NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "is_active" BOOLEAN NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
ALTER TABLE
    "User" ADD CONSTRAINT "user_email_unique" UNIQUE("email");
ALTER TABLE
    "User" ADD CONSTRAINT "user_username_unique" UNIQUE("username");
CREATE TABLE "Exercise"(
    "id" UUID NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "workout" UUID NOT NULL
);
ALTER TABLE
    "Exercise" ADD PRIMARY KEY("id");
CREATE TABLE "Workouts"(
    "id" UUID NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "musle_group" UUID NOT NULL,
    "user" UUID NOT NULL
);
ALTER TABLE
    "Workouts" ADD PRIMARY KEY("id");
CREATE TABLE "Workout_muscle"(
    "id" UUID NOT NULL,
    "workout" UUID NOT NULL,
    "muscle" UUID NOT NULL
);
ALTER TABLE
    "Workout_muscle" ADD PRIMARY KEY("id");
ALTER TABLE
    "Workouts" ADD CONSTRAINT "workouts_musle_group_foreign" FOREIGN KEY("musle_group") REFERENCES "Workout_muscle"("muscle");
ALTER TABLE
    "Workout_muscle" ADD CONSTRAINT "workout_muscle_workout_foreign" FOREIGN KEY("workout") REFERENCES "Muscle_Group"("muscle");
ALTER TABLE
    "Workouts" ADD CONSTRAINT "workouts_user_foreign" FOREIGN KEY("user") REFERENCES "User"("id");
ALTER TABLE
    "Exercise" ADD CONSTRAINT "exercise_workout_foreign" FOREIGN KEY("workout") REFERENCES "Workouts"("id");
ALTER TABLE
    "Set" ADD CONSTRAINT "set_exercise_foreign" FOREIGN KEY("exercise") REFERENCES "Exercise"("id");
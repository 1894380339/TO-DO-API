use mydata

INSERT INTO api_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES
(1, 'pbkdf2_sha256$320000$tLV28TmNri6f6LxJSVsF1D$eBvFPEHakO233ZBV79sh0tDYRf2bPsMmOgutcSpQdUc=', '2022-04-05 17:27:50.095929', 1, 'huan', '', '', 'duonghuan.tl@gmail.com', 1, 1, '2022-04-05 04:18:53.359537'),
(2, 'pbkdf2_sha256$320000$UWL4AxjPQw2wucbJYQpUtj$ukXeayfbqawWkOlAcOVWfTTRnC/nVe6WdWVSDXxa/M4=', NULL, 0, 'huan1', '', '', 'huan1@gmail.com', 0, 1, '2022-04-05 04:23:33.519408'),
(3, '123', '2022-04-05 07:17:10.000000', 0, 'huan3', '', '', '', 0, 1, '2022-04-05 07:17:05.000000'),
(8, 'pbkdf2_sha256$320000$L6YZFwsPxNYIgsbdhuctoY$WNkFzlC+6GsxE1bhEiGVlKNBKGlam6TXHj4jrWShjFA=', NULL, 0, 'Duong_Phuc_Huan', '', '', 'huanduong.tl@gmail.com', 0, 1, '2022-04-05 15:35:14.027313');

INSERT INTO api_task (id, name_task, Description_of_task, Date_of_completion, Status, Date_of_creation, Date_of_modification, user_id) VALUES
(6, 'taske for user 3', 'to do task USER 3', '2022-04-07 08:21:30.000000', 0, '2022-04-05 07:17:42.466131', '2022-04-05 17:28:07.013491', 3),
(9, 'Update Task for completed Task, user Duong_Phuc_Huan', 'Update To_do Task', '2022-04-07 08:21:30.000000', 1, '2022-04-05 15:42:07.006782', '2022-04-05 17:28:32.287895', 2),
(2, 'taske for user 2', 'to do task USER 2', '2022-04-07 08:21:30.000000', 0, '2022-04-05 07:17:42.466131', '2022-04-05 17:28:07.013491', 2);

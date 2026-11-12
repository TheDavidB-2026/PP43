#სავარჯიშო 1
# import time
# import threading
#
# def make_tea(name, seconds):
#     print(f"{name}: იწყება")
#     time.sleep(seconds)
#     print(f"{name}: მზადაა")
#
# teas = [
#     ("მწვანე ჩაი", 1.0),
#     ("შავი ჩაი", 1.5),
#     ("ბალახის ჩაი", 2.0)
# ]
#
# print("--- თანმიმდევრული მომზადება ---")
# start_seq = time.time()
# for name, secs in teas:
#     make_tea(name, secs)
# seq_time = time.time() - start_seq
# print(f"თანმიმდევრულად: {seq_time:.1f} წმ\n")
#
# print("--- Thread-ებით მომზადება ---")
# start_threads = time.time()
# threads = []
#ამის მერე ვეღარ მივხვდი

#სავარჯიშო 2
# import multiprocessing
# import threading
# import time
#
# def cpu_task(n):
#   while n > 0:
#     n -= 1
#
#
# def io_task(seconds):
#   time.sleep(seconds)
#
# def run_sequential(task, jobs):
#   for job in jobs:
#     task(job)
#
#
# def run_threads(task, jobs):
#   threads = []
#   for job in jobs:
#     t = threading.Thread(target=task, args=(job,))
#     threads.append(t)
#     t.start()
#   for t in threads:
#     t.join()
#
#
# def run_processes(task, jobs):
#   processes = []
#   for job in jobs:
#     p = multiprocessing.Process(target=task, args=(job,))
#     processes.append(p)
#     p.start()
#   for p in processes:
#     p.join()
#
# def measure(runner, task, jobs):
#   start_time = time.time()
#   runner(task, jobs)
#   end_time = time.time()
#   return end_time - start_time
#
#
# if __name__ == '__main__':
#   cpu_jobs = [10_000_000] * 4
#   io_jobs = [1.0] * 4
#
#   seq_cpu = measure(run_sequential, cpu_task, cpu_jobs)
#   thr_cpu = measure(run_threads, cpu_task, cpu_jobs)
#   pro_cpu = measure(run_processes, cpu_task, cpu_jobs)
#
#   seq_io = measure(run_sequential, io_task, io_jobs)
#   thr_io = measure(run_threads, io_task, io_jobs)
#   pro_io = measure(run_processes, io_task, io_jobs)
#
#   print(
#       '|              | თანმიმდევრულად        | thread-ები           |'
#       ' პროცესები           '
#   )
#   print(
#       f'| CPU-bound    | {seq_cpu:.2f} წმ ( 1.0x) | {thr_cpu:.2f} წმ'
#       f' ({seq_cpu/thr_cpu:.1f}x) | {pro_cpu:.2f} წმ ({seq_cpu/pro_cpu:.1f}x) |'
#   )
#   print(
#       f'| I/O-bound    | {seq_io:.2f} წმ ( 1.0x) | {thr_io:.2f} წმ'
#       f' ({seq_io/seq_io/thr_io if thr_io>0 else 1:.1f}x) | {pro_io:.2f} წმ'
#       f' ({seq_io/pro_io:.1f}x) |'
#   )
#პასუხი კითხვაზე:
#პაითონში არსებული GIL არ აძლევს რამდენიმე thread-ს ერთდროული ინტენსიური მუშაობის "ნებართვას" ად CPU-BOUND უფრო ნელა სრულდება. ეს პრობლემა არ არის IO-bound შემთხვევაში
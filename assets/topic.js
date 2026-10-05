// Shared behaviour for exam-topic explainers: self-check quizzes and segmented controls.
(function () {
  // Quiz: <div class="q"><p>…</p><div class="opts"><button class="opt" data-correct>…</button>…</div><p class="why">…</p></div>
  const quizzes = document.querySelectorAll(".quiz");
  quizzes.forEach((quiz) => {
    const qs = quiz.querySelectorAll(".q");
    const score = quiz.parentElement.querySelector(".score");
    let answered = 0, right = 0;
    const update = () => { if (score) score.textContent = `${right} / ${qs.length} correct` + (answered < qs.length ? ` · ${qs.length - answered} to go` : ""); };
    qs.forEach((q) => {
      const opts = q.querySelectorAll(".opt");
      opts.forEach((b) => {
        b.type = "button";
        b.addEventListener("click", () => {
          if (q.classList.contains("done")) return;
          q.classList.add("done");
          answered++;
          if (b.hasAttribute("data-correct")) { b.classList.add("right"); right++; }
          else {
            b.classList.add("wrong");
            q.querySelector(".opt[data-correct]")?.classList.add("right");
          }
          opts.forEach((o) => (o.disabled = true));
          update();
        });
      });
    });
    update();
    const reset = quiz.parentElement.querySelector("[data-quiz-reset]");
    reset?.addEventListener("click", () => {
      answered = right = 0;
      qs.forEach((q) => {
        q.classList.remove("done");
        q.querySelectorAll(".opt").forEach((o) => { o.disabled = false; o.classList.remove("right", "wrong"); });
      });
      update();
    });
  });

  // Segmented control: <div class="seg" data-target="name"><button data-value="a">…</button></div>
  // Shows elements with [data-show-name="a"], hides other values, and fires a "segchange" event.
  document.querySelectorAll(".seg[data-target]").forEach((seg) => {
    const name = seg.dataset.target;
    const buttons = seg.querySelectorAll("button[data-value]");
    const select = (v) => {
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.value === v)));
      document.querySelectorAll(`[data-show-${name}]`).forEach((el) => {
        // toggleAttribute (not .hidden) so this also works on SVG elements
        el.toggleAttribute("hidden", !el.getAttribute(`data-show-${name}`).split(" ").includes(v));
      });
      seg.dispatchEvent(new CustomEvent("segchange", { detail: v, bubbles: true }));
    };
    buttons.forEach((b) => { b.type = "button"; b.addEventListener("click", () => select(b.dataset.value)); });
    const initial = seg.querySelector('button[aria-pressed="true"]') || buttons[0];
    if (initial) select(initial.dataset.value);
  });
})();
